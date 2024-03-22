<script setup>
import {useQuery} from "@vue/apollo-composable";
import gql from "graphql-tag";
import {ref, watch} from "vue";
import DataTable from "@/components/DataTable";

const brokers = ref("")
const queryOptions = ref({
  sortBy: null,
  filters: [],
  offset: 0
})
function applyQueryFilter(column, value) {
  console.log(column, value)
}
const { result } = useQuery(gql`
      query getBrokers($options: QueryOptions!) {
        brokers(options: $options) {
          items {
            id
            name
            phoneNumber
            notes
          }
        }
      }`, {
  options: queryOptions
})
watch(result, () => {
  brokers.value = result.value.brokers.items
})

const columns = [
    { name: "Nazwa", sortable: true, model: "name", filterable: true, type: "text"},
    { name: "Telefon", sortable: false, model: "phoneNumber", type: "text"},
    { name: "Notatki", sortable: false, model: "notes", type: "text"},
]
</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Start</a></li>
      <li class="breadcrumb-item active" aria-current="page">Lista pośredników</li>
    </ol>
  </nav>
  <div class="card">
    <div class="card-header">Lista pośredników</div>
    <div class="card-body">
      <RouterLink class="btn btn-primary mb-2" to="posrednicy/dodaj">
        <i class="bi bi bi-plus"></i>Dodaj
      </RouterLink>
      <data-table :columns="columns" :rows="brokers || []" :add-actions-slot="true"
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
