<template>
  <form class="login">
    <h3>Login</h3>

    <input type="email" placeholder="Correo electrónico" v-model="Correo" />
    <input type="password" placeholder="Contraseña" v-model="Contrasena" />
    <button v-on:click="submit">Login</button>
  </form>
  <Alert :error="error"></Alert>
</template>

<script>
import Alert from '../components/alert.vue'

export default {
  data() {
    return {
      Correo: "",
      Contrasena: "",
      error: "",
    };
  },
  components: {
    Alert
  },
  methods: {
    submit: function (event) {
      event.preventDefault();
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
form{
    height: 520px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
}
form *{
    font-family: 'Poppins',sans-serif;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}
form h3{
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label{
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}
input{
    font-weight: bolder;
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
    color: #EEEEEE;

}
::placeholder{
    color: #EEEEEE;
}
button{
    margin-top: 50px;
    width: 100%;
    background-color: #4ECCA3;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
}

button:hover{
    box-shadow: #4ECCA3 0 0 5px;
}
</style>
