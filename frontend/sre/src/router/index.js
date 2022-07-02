import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/home.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/login.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/register.vue"),
  },

  {
    path: "/:pathMatch(.*)*",
    name: "error_404",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/error_404.vue"),
  },
  {
    path: "/estacionamiento",
    name: "estacionamiento",
    meta: {
      requiresAuth: true,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/estacionamiento.vue"),
  },
  {
    path: "/autos",
    name: "autos",
    meta: {
      requiresAuth: true,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/autos.vue"),
  },
  {
    path: "/reservas",
    name: "reservas",
    meta: {
      requiresAuth: true,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/reservas.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to) => {
  if (to.meta.requiresAuth && !store.getters.getAuth) {
    return {
      name: "login",
    };
  }
});

export default router;
