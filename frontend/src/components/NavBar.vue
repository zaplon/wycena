<template>
  <nav class="navbar fixed-bottom navbar-light bg-white">
    <a class="navbar-brand" href="#">
      <img src="@/assets/logo.png">
    </a>
    <div class="d-flex justify-content-around nav-links">
      <router-link to="/wyceny" class="nav-link">Wyceny</router-link>
      <router-link to="/baza-transakcji" class="nav-link">Baza transakcji</router-link>
      <router-link to="/posrednicy" class="nav-link">Pośrednicy</router-link>
      <router-link to="/klienci" class="nav-link">Klienci</router-link>
    </div>
  </nav>
</template>
<style scoped>
 img {
   height: 32px;
 }
 .nav-links {
   width: calc(100% - 40px);
 }
 nav {
 box-shadow: rgba(0, 0, 0, 0.1) 0px -20px 25px -5px, rgba(0, 0, 0, 0.04) 0px -10px 10px -5px;
 }
</style>
