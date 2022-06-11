<template>
  <NavBar :user="user['nombe']"></NavBar>
  <router-view></router-view>
</template>

<script>
import NavBar from './components/NavBar.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap.min.js"
import "bootstrap/dist/js/bootstrap.bundle.min.js"
import "bootstrap"

export default {
  data() {
    return {
      user: {}
    }
  },
  components: {
    NavBar
  },
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #EEEEEE;
  background-color: #232931;
}

nav {
  padding: 30px;
}

.nav-link {
  margin: 15px;
  text-decoration: none;
  font-weight: bold;
  color: #EEEEEE;
}
.router-link-exact-active {
  color: #4ECCA3 !important;
}
</style>
