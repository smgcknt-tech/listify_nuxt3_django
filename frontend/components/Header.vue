<template>
  <div>
    <ul>
      <li @click="open = !open" class="menu-btn">
        <span :class="open ? 'mdi mdi-close' : 'mdi mdi-menu'"></span>
      </li>
      <li>Listify</li>
    </ul>
  </div>
</template>
<script setup>
const open = useHeaderOpen()
</script>

<style lang="scss" scoped>
.menu-btn {
  z-index: 2;
}
</style>
