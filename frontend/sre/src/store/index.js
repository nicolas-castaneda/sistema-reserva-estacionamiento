import { createStore } from "vuex";
import createPersistedStore from "vuex-persistedstate";

export default createStore({
  state: {
    auth: false,
    user: {
      id: null,
      nombres: null,
      correo: null,
      token: null,
    },
  },
  getters: {
    getUser(state) {
      return state.user;
    },
    getUserId(state) {
      return state.user.id;
    },
    getAuth(state) {
      return state.auth;
    },
  },
  mutations: {
    login(state, user) {
      state.auth = true;
      state.user = user;
    },
    logout(state) {
      state.user.id = null;
      state.user.nombres = null;
      state.user.correo = null;
      state.user.token = null;
      state.auth = false;
    },
  },
  actions: {},
  modules: {},
  plugins: [createPersistedStore()],
});
