<script setup>
import {useQuery} from "@vue/apollo-composable";
import gql from "graphql-tag";
import {ref, watch} from "vue";
import DataTable from "@/components/DataTable";
import {openModal} from "@kolirt/vue-modal";
import ImportTransactionsModal from "@/components/modals/ImportTransactionsModal"
import axios from "axios";
import {useNotification} from "@kyvg/vue3-notification";

const transactions = ref("")
const queryOptions = ref({
  sortBy: null,
  filters: null,
  page: 0
})
const {result} = useQuery(gql`
      query getTransactions($options: queryOptions) {
        transactions {
          city
          street
          buildingNumber
          transactionDatetime
          type
          price
          provider
        }
      }`, {
  options: queryOptions
})
watch(result, () => {
  transactions.value = result.value.transactions
})

const { notify }  = useNotification()

function importTransactions() {
  openModal(ImportTransactionsModal).then((data) => {
    const formData = new FormData();
    for (let file of data.file) {
      formData.append('files', file)
    }
    const headers = { 'Content-Type': 'multipart/form-data' };
    axios.post(`${process.env.VUE_APP_BACKEND_URL}/upload/transactions/`, formData, { headers }).then(() => {
      notify("Transakcje zostały zaimportowane")
    }).catch((error) => {
      notify({text:`Wystąpił błąd podczas importu transakcji: ${error}`, type: 'warn'})
    })
  }).catch(()=> {})
}
function onDataFiltering(filters) {
 queryOptions.value.filters = filters
}


const columns = [
  {name: "Miejscowość", sortable: true, model: "city", filterable: true, type: "text"},
  {name: "Ulica", sortable: true, model: "street", filterable: true, type: "text"},
  {name: "Numer", sortable: false, model: "buildingNumber", type: "number"},
  {
    name: "Typ nieruchomości", sortable: false, model: "type", filterable: true,
    filterOptions: [
      {name: "Mieszkania", value: "apartments"},
      {name: "Domy", value: "houses"},
      {name: "Lokale użytkowe", value: "commercial"}
    ]
  },
  {name: "Źródło", sortable: true, model: "provider"},
  {name: "Data transakcji", sortable: true, model: "transactionDatetime"},
  {name: "Cena", sortable: true, model: "price", filterable: true, rangeFilter: true},
]
</script>
<template>
  <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
      <li class="breadcrumb-item"><a href="#">Start</a></li>
      <li class="breadcrumb-item active" aria-current="page">Baza transakcji</li>
    </ol>
  </nav>
  <div class="card">
    <div class="card-header">Baza transakcji</div>
    <div class="card-body">
      <button class="btn btn-primary mb-2" @click="importTransactions">
        <i class="bi bi-cloud-upload me-1"></i>
        Import transakcji
      </button>
      <router-link to="/transakcje/dodaj/" class="ms-1 btn btn-primary mb-2">
        <i class="bi bi-plus me-1"></i>
        Dodaj ręcznie
      </router-link>
      <data-table :columns="columns" :rows="transactions || []" :add-actions-slot="true"
      @filter="onDataFiltering">
        <template v-slot:actions>
          <button class="btn btn-sm btn-danger">
            <i class="bi bi-trash"></i>
          </button>
        </template>
      </data-table>
    </div>
  </div>
</template>
