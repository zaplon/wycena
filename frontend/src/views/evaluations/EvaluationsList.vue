<script setup>
import {useQuery} from "@vue/apollo-composable";
import gql from "graphql-tag";
import {ref, watch} from "vue";
import DataTable from "@/components/DataTable";

const evaluations = ref("")
const queryOptions = ref({
  sortBy: null,
  filters: [],
  offset: 0
})
function applyQueryFilter(column, value) {
  console.log(column, value)
}
const { result } = useQuery(gql`
      query getEvaluations($options: QueryOptions!) {
        evaluations(options: $options) {
          items {
            address
            type
            provider
            paid
          }
        }
      }`, {
  options: queryOptions
})
watch(result, () => {
  evaluations.value = result.value.evaluations
})

const columns = [
    { name: "Adres", sortable: true, model: "address", filterable: true, type: "text"},
    { name: "Typ nieruchomości", sortable: false, model: "type", filterable: true,
      filterOptions: [
          {name: "Mieszkania", value: "apartments"},
          {name: "Domy", value: "houses"},
          {name: "Lokale użytkowe", value: "commercial"}
      ]
    },
    { name: "Źródło", sortable: true, model: "provider"},
    { name: "Data zgłoszenia", sortable: true, model: "date"},
    { name: "Wizja", sortable: false, model: "vision", filterable: true},
    { name: "Operat", sortable: false, model: "finished", filterable: true},
    { name: "Opłacono", sortable: false, model: "paid", filterable: true},
]
</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Start</a></li>
      <li class="breadcrumb-item active" aria-current="page">Lista wycen</li>
    </ol>
  </nav>
  <div class="card">
    <div class="card-header">Lista wycen</div>
    <div class="card-body">
      <router-link class="btn btn-primary mb-2" to="/wyceny/dodaj/">
        <i class="bi bi bi-plus"></i>Dodaj
      </router-link>
      <data-table :columns="columns" :rows="evaluations || []" :add-actions-slot="true"
                  @sort="s => queryOptions.sortBy = s"
                  @paginate="p => queryOptions.page = p"
                  @filter="(c, v) => applyQueryFilter(c,v)">
        <template v-slot:actions>
          <button class="btn btn-sm btn-danger">
            <i class="bi bi-trash"></i>
          </button>
        </template>
      </data-table>
    </div>
  </div>
</template>
