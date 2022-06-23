<template>
  <form class="login" v-on:submit="submit">
    <transition name="slide-fade" appear>
      <h3>Login</h3>
    </transition>

    <input
      class="form-control"
      type="email"
      placeholder="Correo electrónico"
      v-model="Correo"
    />
    <input
      class="form-control"
      type="password"
      placeholder="Contraseña"
      v-model="Contrasena"
    />
    <button>Login</button>
    <p style="padding: 15px">
      No tienes una cuenta?
      <router-link class="link-light" to="/register">Registrate</router-link>
    </p>
  </form>
  <Alert :error="error" v-if="!ok"></Alert>
</template>

<script>
import Alert from "../components/alert.vue";

export default {
  data() {
    return {
      Correo: "",
      Contrasena: "",
      error: null,
      ok: false,
    };
  },
  components: {
    Alert,
  },
  methods: {
    submit: function (event) {
      event.preventDefault();
      this.error = null;
      fetch("http://localhost:5000/session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          correo: this.Correo,
          contrasena: this.Contrasena,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data.success) {
            this.ok = true;
            /*const user = {
              id: data.user.idUsuario,
              correo: data.user.correo,
              nombres: data.user.nombres,
              token: data.token,
            };*/
            this.$store.commit("setUser", data.user);
            this.$router.push("/");
          } else {
            this.error = data.message;
          }
        });
    },
  },
};
</script>

<style scoped>
form {
  height: 520px;
  width: 400px;
  background-color: rgba(255, 255, 255, 0.13);
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  padding: 50px 35px;
}
form * {
  font-family: "Poppins", sans-serif;
  letter-spacing: 0.5px;
  outline: none;
  border: none;
}
form h3 {
  font-size: 32px;
  font-weight: 500;
  line-height: 42px;
  text-align: center;
}

label {
  display: block;
  margin-top: 30px;
  font-size: 16px;
  font-weight: 500;
}
input {
  font-weight: bolder;
  display: block;
  height: 50px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.07) !important;
  border-radius: 3px;
  padding: 0 10px;
  margin-top: 8px;
  font-size: 14px;
  font-weight: 300;
  color: #eeeeee !important;
}
::placeholder {
  color: #eeeeee !important;
}
button {
  margin-top: 50px;
  width: 100%;
  background-color: #4ecca3;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  box-shadow: #4ecca3 0 0 5px;
}
</style>
