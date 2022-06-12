import { createStore } from "vuex";

export default createStore({
  state: {
    user:{
      id: null,
      nombres: "",
      correo: ""
    },
  },
  getters: {
    getUser(state) {
      return state.user;
    },
    getUserId(state) {
      return state.user.id;
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {},
  modules: {},
});
