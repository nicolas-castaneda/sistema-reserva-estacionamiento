<template>
  <form class="register" novalidate v-on:submit="submit">
    <h3>Register</h3>
    <input
      class="form-control shadow-none"
      type="text"
      placeholder="DNI"
      minlength="8"
      maxlength="8"
      v-model="DNI"
      v-on:keypress="numericInput"
      required
    />
    <input
      class="form-control shadow-none"
      type="text"
      placeholder="Celular"
      minlength="9"
      maxlength="9"
      v-model="Celular"
      v-on:keypress="numericInput"
      required
    />
    <input
      class="form-control shadow-none"
      type="text"
      placeholder="Nombres"
      maxlength="50"
      v-model="Nombres"
      required
    />
    <input
      class="form-control shadow-none"
      type="email"
      placeholder="Correo electrónico"
      maxlength="50"
      v-model="Correo"
      required
    />
    <input
      class="form-control shadow-none"
      type="password"
      placeholder="Contraseña"
      minlength="5"
      maxlength="20"
      v-model="Contrasena"
      required
    />
    <button>Register</button>
  </form>
  <Alert :error="error"></Alert>
</template>
<script>
import Alert from "../components/alert.vue";

export default {
  data() {
    return {
      DNI: "",
      Celular: "",
      Nombres: "",
      Correo: "",
      Contrasena: "",
      error: "",
    };
  },
  components: {
    Alert,
  },
  methods: {
    submit: function (event) {
      event.preventDefault();
      this.error = "";
      fetch("http://localhost:5000/usuario", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          DNI: this.DNI,
          celular: this.Celular,
          nombres: this.Nombres,
          correo: this.Correo,
          contrasena: this.Contrasena,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data.success) {
            this.$router.push("/login");
          } else {
            this.error = data.message;
          }
        });
    },
    numericInput: function (event) {
      if (event.code.slice(0, 5) != "Digit") {
        event.preventDefault();
      }
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
