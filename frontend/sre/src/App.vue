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
    return {};
  },
  mounted() {
    this.token = this.$store.state.user.token;
    if (this.token !== null) {
      console.log(this.token);
      fetch("http://localhost:5000/session", {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + this.token,
        },
        body: JSON.stringify({
          correo: this.$store.state.user.correo,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (!data.success) {
            this.$store.commit("logout");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    }
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
  box-shadow: 0 0 0 0.2rem #eeeeee;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
