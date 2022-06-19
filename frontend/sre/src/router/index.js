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
    path: "/:pathMatch(.*)*",
    name: "error_404",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/error.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
