<template>
  <div class="corner" :style="cssVars">
    <Wave v-for="item in gradients" :key="item.viewBox" v-bind="item" :fuzz="fuzz" />
  </div>
</template>

<script>
   export default {
      props: ['position', 'variation', 'fuzz'],
      data() {
        return {
          gradients: [
            {
              viewBox: "0 24 50 35",
              gradient: [
                { offset: "0%", style: "stop-color:#cb6ce6;stop-opacity:1" },
                { offset: "100%", style: "stop-color:#5ce1e6;stop-opacity:1" },
              ],
            },{
              viewBox: "0 24 30 48",
              direction: 'reverse',
              duration: 5000,
              gradient: [
                { offset: "0%", style: "stop-color:#ffd319;stop-opacity:1", },
                { offset: "100%", style: "stop-color:#c233b4;stop-opacity:1", },
              ],
            },
          ]
        }
      },
      computed: {
        cssVars() {
          return this.$R.cond([
            [
              this.$R.whereEq({ position: 'topleft' }), 
              this.$R.always({ '--transform': 'rotate(135deg)', top: '-500px', left: '-500px' })
            ],
            [
              this.$R.whereEq({ position: 'bottomright' }), 
              this.$R.always({ '--transform': 'rotate(315deg)', top: 'calc(100% - 500px)', left: 'calc(100% - 500px)' })
            ],
          ])(this)
        }
      }
   }
</script>

<style>
.corner {
  position: absolute;
  height: 500px;
  width: 1000px;
  overflow: hidden;
  transform-origin: center bottom;
  transform: var(--transform);
  top: var(--top);
  left: var(--left);
}
</style>