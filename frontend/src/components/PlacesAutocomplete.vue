<script setup>
/* eslint-disable no-undef */
import {onMounted, ref, watch, defineEmits} from "vue"

const emit = defineEmits(["selected"])
const place = ref("")
onMounted(() => {
  let autocomplete = new google.maps.places.Autocomplete(
      document.getElementById("places-autocomplete"),
  );
  autocomplete.setComponentRestrictions({ country: ["pl"] })
})
function onPressEnter(event) {
  event.preventDefault()
}
watch(place, () => emit("selected", place.value))
</script>
<template>
  <input @keydown.enter="onPressEnter" type="text" v-model="place" class="form-control" id="places-autocomplete"/>
</template>