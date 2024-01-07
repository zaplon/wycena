<script setup>
import {closeModal, confirmModal} from '@kolirt/vue-modal'
import {ref} from "vue";

const propertyType = ref("")
const city = ref("")
const files = ref([])
function validateForm() {
  let form = document.getElementById('transactions-import')
  form.checkValidity()
  form.classList.add('was-validated')
  confirmModal({city: city.value, propertyType: propertyType.value, files: files.value})
}
const getSelectedFiles = (event) => {
  files.value = event.target.files
}

</script>

<template>
  <SimpleModal title="Import transakcji" size="sm">
    <form id="transactions-import">
      <div class="form-group mb-2">
        <label>Plik(i)</label>
        <input type="file" required class="form-control form-control-sm" multiple accept=".xlsx,.xls,.csv"
               @change="getSelectedFiles">
        <small class="form-text text-muted">Wspierane rozszerzenia: *.xls, *.xlsx, *.csv</small>
        <div class="invalid-feedback">
          Proszę wybrać plik
        </div>
      </div>
      <div class="form-group mb-2">
        <label>Miejscowość</label>
        <input type="text" class="form-control form-control-sm" v-model="city">
      </div>
      <div class="form-group">
        <label>Typ nieruchomości</label>
        <select v-model="propertyType" class="form-select-sm form-select">
          <option value="apartment">Mieszkania</option>
          <option value="houset">Domy</option>
          <option value="commercial">Lokale użytkowe</option>
        </select>
      </div>
    </form>
    <template #footer>
      <button @click="validateForm()" class="btn btn-primary">
        Importuj
      </button>
      <button @click="closeModal()" class="ms-1 btn btn-secondary">
        Zamknij
      </button>
    </template>
  </SimpleModal>
</template>