import { buildUrl } from '../utils/api'

export const state = () => ({
    loading: false,
    comments: {}
})

export const mutations = {
    startLoading(state) {
        state.loading = true
    },
    finishLoading(state, { data, id } = {}) {
        state.loading = false
        if (data) {
            state.comments = {
                ...state.comments,
                [id]: data
            }
        }
    },
    pushComment(state, { comment, id }) {
        let comments = state.comments[id] || {}
        comments = [].concat(comments).concat(comment)

        state.comments = Object.assign(
            {},
            state.comments,
            {
                [id]: comments
            }
        )
    },
}

export const actions = {
    async loadComments({ commit }, { id }) {
        commit('startLoading')

        const data = await this.$http.$get(buildUrl('comments', id))

        commit('finishLoading', { data, id })
    },
    async postComment({ commit }, { id, comment }) {
        commit('startLoading')
        const newComment = await this.$http.$post(buildUrl('comments', id), comment)
        commit('pushComment', { comment: newComment, id })
        commit('finishLoading', { id })
    },
}