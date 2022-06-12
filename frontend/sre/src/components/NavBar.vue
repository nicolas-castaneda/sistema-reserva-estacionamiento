<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item dropdown" v-if="user">
            <a
              class="nav-link dropdown-toggle"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Reservas
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li>
                <router-link to="/principal" class="dropdown-item"
                  >Principal</router-link
                >
              </li>
              <li><hr class="dropdown-divider" /></li>
              <li>
                <router-link to="/reservas" class="dropdown-item"
                  >Mis reservas</router-link
                >
              </li>
              <li>
                <router-link to="/autos" class="dropdown-item"
                  >Mis autos</router-link
                >
              </li>
            </ul>
          </li>
          <li class="nav-item" v-if="user">
            <router-link to="/logout" class="nav-link">Logout</router-link>
          </li>

          <li class="nav-item" v-if="!user">
            <router-link to="/register" class="nav-link">Register</router-link>
          </li>
          <li class="nav-item" v-if="!user">
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
        </ul>
        <span class="navbar-text" v-if="user">
          Hola <strong>{{ user }}</strong>!!!
        </span>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      current_url: window.location.pathname,
    };
  },
  props: {
    user: Object,
  },
};
</script>
