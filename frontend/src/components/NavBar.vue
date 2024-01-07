<template>
  <nav class="navbar fixed-bottom navbar-light bg-light">
    <a class="navbar-brand" href="#">
      <img src="@/assets/logo.png">
    </a>
    <div class="d-flex justify-content-around nav-links">
      <router-link to="/wyceny" class="nav-link">Wyceny</router-link>
      <router-link to="/baza-transakcji" class="nav-link">Baza transakcji</router-link>
      <router-link to="/ustawienia" class="nav-link">Ustawienia</router-link>
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
</style>
