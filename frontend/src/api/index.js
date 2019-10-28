import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  signup(profile) {
        return axios.post(`${apiUrl}/auth/signup/`, {
            profile
        })
    },
    login(profile) {
        return axios.post(`${apiUrl}/auth/login/`, {
            profile
        })
    },
}