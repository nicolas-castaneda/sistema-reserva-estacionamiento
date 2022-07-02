<template>
  <transition name="slide-down" appear>
    <nav class="navbar sticky-top navbar-expand-md navbar-dark bg-dark">
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
              <ul
                class="dropdown-menu animate slideIn"
                aria-labelledby="navbarDropdown"
              >
                <li>
                  <router-link to="/estacionamiento" class="dropdown-item"
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
              <a
                id="logout"
                @click="
                  this.$store.commit('logout');
                  this.$router.push('/');
                "
                class="nav-link"
                >Logout</a
              >
            </li>

            <li class="nav-item" v-if="!user">
              <router-link to="/register" class="nav-link"
                >Register</router-link
              >
            </li>
            <li class="nav-item" v-if="!user">
              <router-link to="/login" class="nav-link">Login</router-link>
            </li>
          </ul>
          <Transition name="slide-fade">
            <span class="navbar-text" v-if="user">
              Hola <strong>{{ user }}</strong
              >!!!
            </span>
          </Transition>
        </div>
      </div>
    </nav>
  </transition>
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
    user: String,
  },
};
</script>

<style scoped>
@media (min-width: 768px) {
  .animate {
    animation-duration: 0.3s;
    -webkit-animation-duration: 0.3s;
    animation-fill-mode: both;
    -webkit-animation-fill-mode: both;
  }
}

@keyframes slideIn {
  0% {
    transform: translateY(-2rem);
    opacity: 0;
  }

  100% {
    transform: translateY(0rem);
    opacity: 1;
  }

  0% {
    transform: translateY(-2rem);
    opacity: 0;
  }
}

@-webkit-keyframes slideIn {
  0% {
    -webkit-transform: transform;
    -webkit-opacity: 0;
  }

  100% {
    -webkit-transform: translateY(0);
    -webkit-opacity: 1;
  }

  0% {
    -webkit-transform: translateY(-2rem);
    -webkit-opacity: 0;
  }
}

.slide-down-enter-active {
  transition: all 0.6s ease-out;
}

.slide-down-leave-active {
  transition: all 1s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-down-enter-from,
.slide-down-leave-to {
  transform: translatey(-30px);
  opacity: 0;
}

.slideIn {
  -webkit-animation-name: slideIn;
  animation-name: slideIn;
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

#logout {
  cursor: pointer;
}
#logout:hover {
  color: rgb(235, 62, 62) !important;
}
</style>
