import { createStore } from "vuex";
import createPersistedStore from "vuex-persistedstate";

export default createStore({
  state: {
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
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    logout(state) {
      state.user.id = null;
      state.user.nombres = null;
      state.user.correo = null;
      state.user.token = null;
    },
  },
  actions: {},
  modules: {},
  plugins: [createPersistedStore()],
});
