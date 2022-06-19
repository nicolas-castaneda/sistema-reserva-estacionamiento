<template>
  <NavBar :user="this.$store.state.user.nombres"></NavBar>
  <router-view></router-view>
</template>

<script>
import NavBar from "./components/NavBar.vue";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

export default {
  data() {
    return {
    };
  },
  components: {
    NavBar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #eeeeee;
  background-color: #232931;
  min-width: 550px;
}

nav {
  padding: 30px;
}

.nav-link {
  margin: 15px;
  text-decoration: none;
  font-weight: bold;
  color: #eeeeee;
}
.router-link-exact-active {
  color: #4ecca3 !important;
}

.form-control:focus {
  box-shadow: 0 0 0 0.2rem #EEEEEE;
}
</style>
