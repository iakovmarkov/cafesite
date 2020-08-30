import * as R from 'ramda'

export const state = () => ({
    open: false
})

export const mutations = {
    toggle(state) {
        state.open = R.not(state.open)
    }
}
