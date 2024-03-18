<script setup>
import "leaflet/dist/leaflet.css"
import { LMap } from "@vue-leaflet/vue-leaflet"
import {ref} from "vue";

let zoom = ref(6)
let center = ref([38, 139.69])
</script>
<template>
  <div id="map">
    <l-map ref="map" :zoom="zoom" :center="center" :useGlobalLeaflet="false">
    </l-map>
  </div>
</template>
<style scoped>
  #map {
    height: 200px;
  }
</style>
