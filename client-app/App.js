import "react-native-gesture-handler";
import React, { useEffect } from "react";
import { StatusBar } from "expo-status-bar";
import { NavigationContainer } from "@react-navigation/native";
import DrawerNavigator from "./src/navigators/DrawerScreen";
import { SafeAreaView, Alert, BackHandler } from "react-native";
import Constants from "expo-constants";
import { RootSiblingParent } from "react-native-root-siblings";

const App = () => {
	useEffect(() => {
		const backAction = () => {
			Alert.alert("종료하기", "정말 종료 하시겠습니까?", [
				{
					text: "Cancel",
					onPress: () => null,
					style: "cancel",
				},
				{ text: "YES", onPress: () => BackHandler.exitApp() },
			]);
			return true;
		};

		const backHandler = BackHandler.addEventListener(
			"hardwareBackPress",
			backAction
		);

		return () => backHandler.remove();
	}, []);

	return (
		<SafeAreaView style={{ flex: 1, marginTop: Constants.statusBarHeight }}>
			<RootSiblingParent>
				<NavigationContainer independent={true}>
					<DrawerNavigator />
					<StatusBar style="auto" />
				</NavigationContainer>
			</RootSiblingParent>
		</SafeAreaView>
	);
};

export default App;
