import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/home.vue";

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
    path: "/estacionamiento",
    name: "estacionamiento",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/estacionamiento.vue"),
  },{
    path: "/autos",
    name: "autos",
    component: () =>
      import ( /* webpackChunkName: "about" */"../views/autos.vue"),
  },
  {
    path: "/reservas",
    name: "reservas",
    component: () =>
      import (/* webpackChunkName: "about" */"../views/reservas.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
