import React from "react";
import { createDrawerNavigator } from "@react-navigation/drawer";

import Donga from "../screens/Donga";
import Joseon from "../screens/Joseon";
import Joongang from "../screens/Joongang";
import Busan from "../screens/Busan";
import Hanguk from "../screens/Hanguk";
import Herald from "../screens/Herald";
import Nocut from "../screens/Nocut";
import Ohmynews from "../screens/Ohmynews";
import Wiki from "../screens/Wiki";
import Yeonhap from "../screens/Yeonhap";
import Main from "../screens/Main";
import Subscribe from "../screens/Subscribe";

const Drawer = createDrawerNavigator();

const DrawerNavigator = ({ navigation }) => {
	return (
		<Drawer.Navigator initialRouteName="Main">
			<Drawer.Screen
				name="Main"
				component={Main}
				options={{ drawerLabel: "HOME" }}
			/>
			<Drawer.Screen
				name="Joseon"
				component={Joseon}
				options={{ drawerLabel: "조선일보" }}
			/>
			<Drawer.Screen
				name="Joongang"
				component={Joongang}
				options={{ drawerLabel: "중앙일보" }}
			/>
			<Drawer.Screen
				name="Donga"
				component={Donga}
				options={{ drawerLabel: "동아일보" }}
			/>
			<Drawer.Screen
				name="Pusan"
				component={Busan}
				options={{ drawerLabel: "부산일보" }}
			/>
			<Drawer.Screen
				name="Hanguk"
				component={Hanguk}
				options={{ drawerLabel: "한국일보" }}
			/>
			<Drawer.Screen
				name="Yeonhap"
				component={Yeonhap}
				options={{ drawerLabel: "연합뉴스" }}
			/>
			<Drawer.Screen
				name="Herald"
				component={Herald}
				options={{ drawerLabel: "헤럴드경제" }}
			/>
			<Drawer.Screen
				name="Nocut"
				component={Nocut}
				options={{ drawerLabel: "노컷뉴스" }}
			/>
			<Drawer.Screen
				name="Wiki"
				component={Wiki}
				options={{ drawerLabel: "위키트리" }}
			/>
			<Drawer.Screen
				name="Ohmynews"
				component={Ohmynews}
				options={{ drawerLabel: "오마이뉴스" }}
			/>
			<Drawer.Screen
				name="Subs"
				component={Subscribe}
				options={{ drawerLabel: "구독한 언론사" }}
			/>
		</Drawer.Navigator>
	);
};

export default DrawerNavigator;
