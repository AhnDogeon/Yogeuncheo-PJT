import api from '../../api'

// initial state
const state = {
    // shape: [{ id, title, genres, viewCnt, rating }]
    dong_info: [],
    dong_list: [],
    dong2: [],
    userInfo: JSON.parse(localStorage.getItem('userInfo')),
};

// actions
const actions = {
    async getScoreOfDong({commit}, params) {
        const resp = await api.getScoreOfDong(params);
        console.log(resp)
        commit('getScoreOfDongCommit', resp)
    },

    async getListOfDong({commit}, params) {
        const resp = await api.getListOfDong(params);
        commit('getListOfDongCommit', resp)
    },
    async getDong2({commit}, params) {
        const resp = await api.getDong2(params);
        commit('getDong2Commit', resp)
    },
};

// mutations
const mutations = {
    getScoreOfDongCommit(state, payload) {
        state.dong_info = payload.data
    },
    getListOfDongCommit(state, payload) {
        state.dong_list = payload.data
    },
    getDong2Commit(state, payload) {
        state.dong2 = payload.data
    },
};

export default {
    namespaced: true,
    state,
    actions,
    mutations
}