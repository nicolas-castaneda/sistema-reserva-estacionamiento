<template>
  <NavBar></NavBar>
  <router-view></router-view>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
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

nav a {
  margin: 15px;
  text-decoration: none;
  font-weight: bold;
  color: #EEEEEE;
}

nav a.router-link-exact-active {
  color: #4ECCA3;
}
</style>
