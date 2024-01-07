<script setup>
import {computed, defineEmits, defineProps, ref} from "vue";

const props = defineProps({
  columns: Array,
  rows: Array,
  addActionsSlot: Boolean,
  page: Number,
  totalPages: Number
})
const emit = defineEmits(["paginate", "sort", "filter"])

const paginationLimit = computed(() => {
  if (!props.page || !props.totalPages)
    return 1
  return (props.totalPages - props.page) > 10 ? props.page + 10 : props.totalPages
})
const sortDir = ref("")
function sort(model) {
  if (sortDir.value === model)
    sortDir.value = '-' + model
  else
    sortDir.value = model
  emit("sort", sortDir.value)
}
function paginate(page) {
  emit("paginate", {page: page})
}
function filterData(e, column) {
  emit("filter", {column: column, value: e.target.value})
}
</script>
<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th v-for="col in columns" :key="col.name" :class="{ pointer: col.sortable }" @click="col.sortable ? sort(col.model): null">
          {{ col.name }}
          <i v-if="sortDir === col.model" class="bi bi-arrow-up"></i>
          <i v-if="sortDir === '-' + col.model" class="bi bi-arrow-down"></i>
        </th>
        <th v-if="addActionsSlot"></th>
      </tr>
      <tr>
        <th v-for="col in columns" :key="col.name">
          <template v-if="col.filterable">
            <select class="form-select" v-if="col.filterOptions" @change="filterData(col.model)">
              <option v-for="o in col.filterOptions" value="o.value" :key="o.value">{{ o.name }}</option>
            </select>
            <input type="text" class="form-control" v-else-if="col.type === 'text'" @change="filterData(col.model)">
            <input type="number" class="form-control" v-else-if="col.type === 'number'" @change="filterData(col.model)">
          </template>
        </th>
        <th v-if="addActionsSlot"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in rows" :key="row.id">
        <td v-for="col in columns" :key="col.name">
          {{ row[col.model] }}
        </td>
        <td v-if="addActionsSlot">
          <slot name="actions"></slot>
        </td>
      </tr>
    </tbody>
    <tfoot>
      <nav v-if="page">
        <ul class="pagination">
          <li class="page-item" v-if="page > 1">
            <a class="page-link" @click="paginate(page - 1)">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          <li class="page-item" v-for="page in paginationLimit" :key="page">
            <a class="page-link" @click="paginate(page)">{{ page }}</a>
          </li>
          <li class="page-item" v-if="paginationLimit < totalPages">
            <a class="page-link" @click="paginate(paginationLimit + 1)">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </tfoot>
  </table>
</template>