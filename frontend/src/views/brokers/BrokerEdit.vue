<script setup>
import {useMutation, useQuery} from "@vue/apollo-composable"
import gql from 'graphql-tag'
import {ref, watch} from "vue"
import {useRoute, useRouter} from "vue-router";

const route = useRoute()
const router = useRouter()

const broker = ref({
  id: route.params.id,
  name: "",
  phoneNumber: "",
  notes: ""
})


watch(() => route.params.id, (newId) => {
  broker.value.id = newId
})

const {result, loading, error} = useQuery(gql`
      query getBroker($pk: UUID!) {
        brokerByPk(pk: $pk) {
          id
          name
          phoneNumber
          notes
        }
      }
    `, {
      pk: broker.value.id
    }, () => ({
      enabled: broker.value.id,
    })
)
watch(result, (data) => {
  broker.value = data.brokerByPk
})

const {mutate: saveBrokerMutation} = useMutation(gql`
      mutation saveBroker ($input: JSON!) {
        addInstance (instanceType: BROKER, data: $input)
      }
    `, {variables: {input: broker.value}})

const {mutate: updateBrokerMutation} = useMutation(gql`
      mutation updateBroker ($pk: UUID!, $input: JSON!) {
        updateInstance (instanceType: BROKER, pk: $pk, data: $input)
      }
    `, {variables: {pk: broker.value.id, input: broker.value}})

const {mutate: deleteBrokerMutation} = useMutation(gql`
      mutation deleteBroker ($pk: UUID!) {
        deleteInstance (instanceType: BROKER, pk: $pk)
      }
    `, {variables: {id: broker.value.id}})

function saveBroker(event) {
  event.preventDefault()
  let form = document.getElementById("view-form")
  if (!form.checkValidity()) {
    return
  }
  let mut
  if (broker.value.id)
    mut = updateBrokerMutation()
  else
    mut = saveBrokerMutation()
  mut.then(() => router.push("/posrednicy/"))
}
function removeBroker() {
  deleteBrokerMutation().then(router.push("/posrednicy/"))
}

</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><RouterLink to="/">Start</RouterLink></li>
      <li class="breadcrumb-item"><RouterLink to="/posrednicy/">posrednicy</RouterLink></li>
      <li v-if="!broker.name" class="breadcrumb-item active" aria-current="page">Nowy pośrednik</li>
      <li v-else class="breadcrumb-item active" aria-current="page">{{ broker.name }}</li>
    </ol>
  </nav>
  <div class="card" :class="{'loading-data': loading, 'loading-failed': error}">
    <div class="card-header">
      {{ broker.id ? broker.name : "Nowy pośrednik" }}
    </div>
    <form @submit="saveBroker" id="view-form">
      <div class="card-body">
        <div class="row mb-3 mt-3">
          <div class="col col-md-3">
            <label class="form-label">Nazwa</label>
          </div>
          <div class="col col-md-9">
            <input required type="text" class="form-control" v-model="broker.name">
          </div>
        </div>
        <div class="row mb-3 mt-3">
          <div class="col col-md-3">
            <label class="form-label">Kontaktowy nr telefonu</label>
          </div>
          <div class="col col-md-9">
            <input type="text" class="form-control" v-model="broker.phoneNumber">
          </div>
        </div>
        <div class="row mb-3 mt-3">
          <div class="col col-md-3">
            <label class="form-label">Notatki</label>
          </div>
          <div class="col col-md-9">
            <textarea class="form-control" v-model="broker.notes"></textarea>
          </div>
        </div>
      </div>
      <div class="card-footer">
        <button type="submit" class="btn btn-primary">Zapisz</button>
        <RouterLink to="/posrednicy/" class="btn btn-default">Cofnij</RouterLink>
        <button v-if="broker.id" type="button" @click="removeBroker" class="btn btn-danger float-end">Usuń</button>
      </div>
    </form>
  </div>
</template>
