<template>
  <notifications />
  <div class="container mt-4 mb-4">
    <router-view></router-view>
  </div>
  <NavBar class="ps-4 pe-4"></NavBar>
  <ModalTarget />
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>
