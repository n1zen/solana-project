<template>
    <nav id="nav" class="nav">
        <div id="top">
            <div id="cont-logo">
                <div id="logo">
                    <img src="../../assets/solana_logo_15pt.avif" alt="solana_logo">
                </div>
                <div id="logo-name">
                    Solana Atelier
                </div>
            </div>
            <div id="cont-side-panel">
                <div id="cont-profile-time">
                    <div id="cont-profile-time-upper-section">
                        <img src="../../assets/photos/christina-wocintechchat-com-m-PlikkWB79qs-unsplash.jpg"
                            alt="Profile Picture" id="profile-photo">
                        <div id="date-time">
                            <span id="date">Tue, Mar. 3</span>
                            <span id="time">03:39PM</span>
                        </div>
                    </div>
                    <div id="cont-lower-section">
                        <p id="welcome">
                            Welcome back,
                            <br /><span id="user">Adrenaline</span>!
                        </p>
                    </div>
                </div>
                <div id="cont-pages">
                    <NavButton 
                        text="Dashboard"
                        :is-selected="activeButton === 'Dashboard'" :is-hovered="hoveredButton === 'Dashboard'"
                        :is-blurred="activeButton === 'Dashboard' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'"
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave" 
                        @on-click="changePage">
                        <template #sIcon>
                            <LayoutDashboard color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton
                        text="Lifecycle"
                        :is-selected="activeButton === 'Lifecycle'"
                        :is-hovered="hoveredButton === 'Lifecycle'" 
                        :is-blurred="activeButton === 'Lifecycle' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave" 
                        @on-click="changePage">
                        <template #sIcon>
                            <Recycle color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton 
                        text="Analytics"
                        :is-selected="activeButton === 'Analytics'"
                        :is-hovered="hoveredButton === 'Analytics'"
                        :is-blurred="activeButton === 'Analytics' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage">
                        <template #sIcon>
                            <ChartLine color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton 
                        text="Projects"
                        :is-selected="activeButton === 'Projects'" 
                        :is-hovered="hoveredButton === 'Projects'"
                        :is-blurred="activeButton === 'Projects' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage" >
                        <template #sIcon>
                            <FolderGit2 color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton 
                        text="Teams"
                        :is-selected="activeButton === 'Teams'" 
                        :is-hovered="hoveredButton === 'Teams'"
                        :is-blurred="activeButton === 'Teams' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage">
                        <template #sIcon>
                            <HeartHandshake color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton 
                        text="Inventory"
                        :is-selected="activeButton === 'Inventory'" 
                        :is-hovered="hoveredButton === 'Inventory'"
                        :is-blurred="activeButton === 'Inventory' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage">
                        <template #sIcon>
                            <ShelvingUnit color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                    <NavButton 
                        text="Products"
                        :is-selected="activeButton === 'Products'" 
                        :is-hovered="hoveredButton === 'Products'"
                        :is-blurred="activeButton === 'Products' && activeButton !== hoveredButton && hoveredButton !== null && hoveredButton !== 'Logout'" 
                        @on-hover="buttonOnHover" 
                        @on-leave="buttonOnLeave"
                        @on-click="changePage">
                        <template #sIcon>
                            <PackageSearch color="var(--color-primary)"/>
                        </template>
                    </NavButton>
                </div>
            </div>
        </div>
        <div id="cont-logout">
            <NavButton
                text="Logout" 
                textcolor="#C84A46" 
                :is-hovered="hoveredButton === 'Logout'" 
                :is-logout="true" 
                @on-hover="buttonOnHover"
                @on-leave="buttonOnLeave">
                <template #sIcon>
                    <LogOut color="var(--color-secondary)"/>
                </template>
            </NavButton>
        </div>
    </nav>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { LayoutDashboard, Recycle, PackageSearch, LogOut, ChartLine, FolderGit2, HeartHandshake, ShelvingUnit } from 'lucide-vue-next';

import NavButton from '@/components/Buttons/NavButton/NavButton.vue';

const router = useRouter();
const route = useRoute();

const activeButton = ref('Dashboard'); // Dashboard as default
const hoveredButton = ref(null);

watch(route, () => {
    activeButton.value = route.name.charAt(0).toUpperCase() + route.name.slice(1);
});

// FROM CHILD EMITS
function changePage(pageName) {
    if (activeButton.value === pageName) return;

    activeButton.value = pageName;
    router.push(`/${pageName.toLowerCase()}`)
};

function buttonOnHover(buttonName) {
    hoveredButton.value = buttonName;
}

function buttonOnLeave() {
    hoveredButton.value = null;
}
</script>

<style scoped>
#nav {
    --real-width: 320px;

    height: calc(100dvh - var(--margin-top-main));
    padding-bottom: var(--margin-top-main);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: sticky;
    top: calc(var(--margin-top-main));
}

#cont-logo {
    margin-bottom: 30px;
    width: var(--real-width);
    display: flex;
    align-items: center;
    gap: 17px;
}

#logo {
    aspect-ratio: 1;
    background-color: var(--color-secondary);
    border-radius: 10px;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;

    img {
        width: 30px;
        object-fit: contain;
    }
}

#logo-name {
    color: var(--color-secondary);
    font-family: 'SolanaAtelier', 'sans-serif';
    font-weight: bold;
    font-size: 36px;
}

#cont-side-panel {
    background-color: var(--color-secondary);
    border-radius: 15px;
    width: var(--real-width);
    padding: 20px;
}

#cont-profile-time {
    color: var(--color-primary);
    border-bottom: 2px solid var(--color-primary);
    margin-bottom: 17px;
    padding-bottom: 17px;
}

#cont-profile-time-upper-section {
    padding-bottom: 17px;
    display: flex;
    justify-content: space-between;
}

#date-time {
    text-align: right;
    display: flex;
    flex-direction: column;
}

#profile-photo {
    aspect-ratio: 1;
    border-radius: 5px;
    width: 60px;
    object-fit: cover;
}

#cont-lower-section {
    font-size: 24px;
}

#welcome {
    line-height: 30px;
}

#cont-logout {
    padding-left: 20px;
}
</style>