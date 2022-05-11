<template>
  <aside :class="{ 'is-active': open }">
    <ul class="menu">
      <li>MENU</li>
      <li>MEAL PLAN</li>
      <li>LIST</li>
    </ul>
  </aside>
</template>

<script setup>
const open = useHeaderOpen()
</script>

<style lang="scss" scoped>
aside {
  @include background-color(#555);
  @include row-center;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  transform: translateX(-100vw);
  transition: all 0.2s linear;

  .menu {
    flex-direction: column;
    li {
      @include color;
      @include padding;
      @include font-size(3rem);
    }
  }
  &.is-active {
    transform: translateX(0);
  }
}
</style>
