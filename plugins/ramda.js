import * as R from 'ramda'

/**
 * This will inject `this.$R` Ramda object everywhere
 * To context, to `this` in Vue objects
 * Feels so hacky
 */
export default (context, inject) => {
    inject('R', R)
    context.$R = R
  }
  