<template>
  <div class="position-absolute bottom-0 start-50 translate-middle-x">
    <transition name="bounce">
      <div class="container" v-if="error">
        <div class="alert alert-danger">
          <strong>Error!</strong> {{ error }}
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "error",
  setup() {},
  props: {
    error: String,
  },
};
</script>

<style scoped>
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>
