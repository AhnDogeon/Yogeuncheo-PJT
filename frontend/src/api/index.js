import axios from 'axios'

const apiUrl = '/api';

export default {
  getScoreOfDong(params) {
    return axios.get(`${apiUrl}/score/`, {
      params,
    })
  },

  getListOfDong(params) {
    return axios.get(`${apiUrl}/score/`, {
      params,
    })
  },
  getDong2(params) {
    return axios.get(`${apiUrl}/score/`, {
      params,
    })
  },
}