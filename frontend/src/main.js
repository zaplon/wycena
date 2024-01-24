import {createApp, h, provide} from 'vue'
import App from './App.vue'
import "./assets/scss/theme.scss"
import 'bootstrap-icons/font/bootstrap-icons.css'
import EvaluationsList from './views/evaluations/EvaluationsList'
import EvaluationEdit from './views/evaluations/EvaluationEdit'
import TransactionsList from './views/transactions/TransactionsList'
import {createRouter, createWebHashHistory} from 'vue-router'
import {ApolloClient, createHttpLink, InMemoryCache} from '@apollo/client/core'
import {DefaultApolloClient} from "@vue/apollo-composable";
import {createModal} from "@kolirt/vue-modal";
import {Notifications} from "@kyvg/vue3-notification";

const httpLink = createHttpLink({
  uri: `${process.env.VUE_APP_BACKEND_URL}/graphql`,
})

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
})

const routes = [
  { path: '/', component: EvaluationsList },
  { path: '/wyceny/', component: EvaluationsList },
  { path: '/wyceny/dodaj/', component: EvaluationEdit },
  { path: '/wyceny/:id', component: EvaluationEdit },
  { path: '/baza-transakcji/', component: TransactionsList },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

const app = createApp({
  setup () {
    provide(DefaultApolloClient, apolloClient)
  },
  render: () => h(App),
})

app.use(router)
app.use(createModal())
app.use(Notifications)
app.mount('#app')
