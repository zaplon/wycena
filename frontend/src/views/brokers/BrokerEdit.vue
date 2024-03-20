<script setup>
import {useMutation, useQuery} from "@vue/apollo-composable"
import gql from 'graphql-tag'
import {ref, watch} from "vue"
import {useRoute, useRouter} from "vue-router";
const broker = ref({
  id: null,
  name: "",
  notes: ""
})
const route = useRoute()
const router = useRouter()

const {result, loading, error} = useQuery(gql`
      query getBroker($id: String) {
        brokerById(id: $id) {
          id
          name
          notes
        }
      }
    `, {
      id: route.params.id
    }, () => ({
      enabled: route.params.id,
    })
)
watch(result, (value) => broker.value = value)

const {mutate: saveBrokerMutation} = useMutation(gql`
      mutation saveBroker ($input: JSON!) {
        createInstance (data: $input) {
          id
        }
      }
    `)

const {mutate: updateBrokerMutation} = useMutation(gql`
      mutation updateBroker ($id: UUID!, $input: JSON!) {
        updateInstance (id: $id, data: $input) {
          id
        }
      }
    `)

const {mutate: deleteBrokerMutation} = useMutation(gql`
      mutation deleteBroker ($id: UUID!) {
        deleteInstance (id: $id)
      }
    `)

function saveBroker() {
  let mut
  if (broker.value.id)
    mut = updateBrokerMutation(broker.value.id, broker.value)
  else
    mut = saveBrokerMutation(broker.value)
  mut.then(() => router.push("/posrednicy/"))
}
function removeBroker() {
  deleteBrokerMutation(broker.value.id).then(router.push("/posrednicy/"))
}

</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Start</a></li>
      <li class="breadcrumb-item"><a href="/posrednicy/">Start</a></li>
      <li v-if="!broker.id" class="breadcrumb-item active" aria-current="page">Nowy pośrednik</li>
      <li v-else class="breadcrumb-item active" aria-current="page">{{broker.name }}</li>
    </ol>
  </nav>
  <div class="card" :class="{'loading-data': loading, 'loading-failed': error}">
    <div class="card-header">
      {{ broker.id ? broker.name : "Nowy pośrednik" }}
    </div>
    <form @submit="saveBroker">
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
        <a href="/posrednicy/" class="btn btn-default">Cofnij</a>
        <button v-if="broker.id" type="button" @click="removeBroker" class="btn btn-danger float-end">Usuń</button>
      </div>
    </form>
  </div>
</template>
