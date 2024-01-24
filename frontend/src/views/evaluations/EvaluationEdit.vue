<script setup>
import {useMutation, useQuery} from "@vue/apollo-composable"
import gql from 'graphql-tag'
import {ref, watch} from "vue"
import PlacesAutocomplete from "@/components/PlacesAutocomplete";
import {useRoute} from "vue-router";

const evaluation = ref({
  id: null,
  paid: false,
  address: ""
})
const route = useRoute()

const {result, loading, error} = useQuery(gql`
      query getEvaluation($id: String) {
        evaluationById(id: $id) {
          id
          address
          price
          paid
        }
      }
    `, {
      id: route.params.id
    }, () => ({
      enabled: route.params.id,
    })
)
watch(result, (value) => evaluation.value = value)

const {mutate: saveEvaluationMutation} = useMutation(gql`
      mutation saveEvaluation ($input: SaveEvaluationInput!) {
        saveEvaluation (input: $input) {
          id
        }
      }
    `)

function saveEvaluation() {
  saveEvaluationMutation()
}

function setAddress(address) {
  evaluation.value.address = address
}

</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Start</a></li>
      <li class="breadcrumb-item active" aria-current="page">Nowa wycena</li>
    </ol>
  </nav>
  <div class="card" :class="{'loading-data': loading, 'loading-failed': error}">
    <div class="card-header">
      {{ evaluation.id ? evaluation.address : "Nowa wycena" }}
    </div>
    <form @submit="saveEvaluation">
      <div class="card-body">
        <ul class="nav nav-pills">
          <li class="nav-item">
            <a class="nav-link active" href="#basic-info">Dane podstawowe</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#calculations">Obliczenia</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#photos">Zdjęcia</a>
          </li>
        </ul>

        <div id="basic-info">
          <div class="mb-3 mt-3">
            <label class="form-label">Adres</label>
            <places-autocomplete @selected="setAddress"/>
          </div>
          <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" v-model="evaluation.paid">
            <label class="form-check-label">Opłacone</label>
          </div>
        </div>
      </div>

      <div class="card-footer">
        <button type="submit" class="btn btn-primary">Zapisz</button>
        <button type="submit" class="btn btn-secondary ms-2">Wygeneruj operat</button>
      </div>
    </form>
  </div>
</template>
