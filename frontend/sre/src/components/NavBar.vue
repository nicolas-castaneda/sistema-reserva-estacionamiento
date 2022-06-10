<template>
  <nav>
    <router-link to="/">Home</router-link>
    <span v-if="nombre">
      <h6 class="item left text" v-show="nombre"> Hola {{nombre}}!</h6>
      <router-link to="/reservas">Reservas</router-link>
      <router-link to="/logout">Logout</router-link>
    </span>
    <span v-else>
      <router-link to="/register">Register</router-link>
      <router-link to="/login">Login</router-link>
    </span>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      current_url : window.location.pathname,
    }
  },
  props:{
    nombre: String
  }
}
</script>
