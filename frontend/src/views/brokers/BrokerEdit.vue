<script setup>
import {useMutation, useQuery} from "@vue/apollo-composable"
import gql from 'graphql-tag'
import {ref, watch} from "vue"
import PlacesAutocomplete from "@/components/PlacesAutocomplete";
import {useRoute} from "vue-router";

const broker = ref({
  id: null,
  name: ""
})
const route = useRoute()

const {result, loading, error} = useQuery(gql`
      query getBroker($id: String) {
        brokerById(id: $id) {
          id
          name
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
      mutation saveBroker ($input: SaveBrokerInput!) {
        saveBroker (input: $input) {
          id
        }
      }
    `)

function saveBroker() {
  saveBrokerMutation()
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
      {{ broker.id ? broker.address : "Nowa wycena" }}
    </div>
    <form @submit="saveBroker">
      <div class="card-body">
      </div>
      <div class="card-footer">
        <a href="/posrednicy/" class="btn btn-default">Cofnij</a>
        <button type="submit" class="btn btn-primary">Zapisz</button>
      </div>
    </form>
  </div>
</template>
