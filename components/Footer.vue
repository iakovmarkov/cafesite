<template>
  <footer>
    <div class="waveContainer">
      <Wave v-for="item in gradients" :key="item.viewBox" v-bind="item" />
    </div>
    <div class="textContainer">
      2020. Acid Cafe.
    </div>
  </footer>
</template>

<script>
   export default {
      data() {
        return {
          gradients: [
            {
              viewBox: "0 24 50 35",
              duration: 80000,
              gradient: [
                { offset: "0%", style: "stop-color:#cb6ce6;stop-opacity:1" },
                { offset: "100%", style: "stop-color:#5ce1e6;stop-opacity:1" },
              ],
            },{
              viewBox: "0 24 30 48",
              direction: 'reverse',
              duration: 20000,
              gradient: [
                { offset: "0%", style: "stop-color:#ffd319;stop-opacity:1", },
                { offset: "100%", style: "stop-color:#c233b4;stop-opacity:1", },
              ],
            },
          ]
        }
      },
   }
</script>

<style>
footer {
  position: relative;
  height: 100px;
  display: flex !important;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.waveContainer {
  height: 100px;
  width: 100%;
  position: absolute;
  overflow: hidden;
}

.textContainer {
  z-index: 9999;
  color: #ffffff;
  padding: 10px;
}
</style>
