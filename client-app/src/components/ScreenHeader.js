import React, { useState, useEffect } from "react";
import { View, StyleSheet, Text, Platform, CheckBox } from "react-native";
import { AntDesign } from "@expo/vector-icons";
import AsyncStorage from "@react-native-async-storage/async-storage";

const ScreenHeader = (props) => {
	const [isSelected, setSelection] = useState(false);

	const storeSubScribe = async (value) => {
		try {
			const jsonValue = JSON.stringify(value);
			await AsyncStorage.setItem(props.screenName, jsonValue);
		} catch (e) {
			console.log(e);
		}
	};

	const getSubScribe = async () => {
		try {
			const jsonValue = await AsyncStorage.getItem(props.screenName);
			return jsonValue != null ? JSON.parse(jsonValue) : null;
		} catch (e) {
			console.log(e);
		}
	};

	useEffect(() => {
		let value = getSubScribe();
		if (value != null) {
			if (value[props.screenName] === true) {
				setSelection(true);
			} else {
				setSelection(false);
			}
		}
	}, []);

	useEffect(() => {
		let value = getSubScribe();
		if (value != null) {
			if (isSelected === true) {
				value[props.screenName] = true;
			} else {
				value[props.screenName] = false;
			}
		} else {
			value[props.screenName] = false;
		}
		console.log(value);
		storeSubScribe(value);
	}, [isSelected]);

	return (
		<View style={styles.header}>
			<AntDesign.Button
				name="menuunfold"
				size={24}
				color="black"
				backgroundColor="white"
				onPress={() => props.navigation.toggleDrawer()}
			/>
			<Text style={styles.text}>
				{props.screenName} : {props.categoryLabelValue}
			</Text>
			<View style={styles.subScribe}>
				<Text style={styles.subScribeText}>구독</Text>
				<CheckBox
					value={isSelected}
					onValueChange={setSelection}
					style={styles.subScribeBox}
				/>
			</View>
			<View style={{ flexDirection: "row" }}>
				<AntDesign.Button
					name="search1"
					size={24}
					color="black"
					backgroundColor="white"
					onPress={() => {
						props.FsetVisible2(true);
					}}
				/>
				<AntDesign.Button
					name="appstore1"
					size={24}
					color="black"
					backgroundColor="white"
					onPress={() => props.FsetVisible1(true)}
				/>
			</View>
		</View>
	);
};
let styles;
if (Platform.OS === "android") {
	styles = StyleSheet.create({
		header: {
			width: "100%",
			height: "8.5%",
			backgroundColor: "white",
			alignItems: "center",
			justifyContent: "space-between",
			flexDirection: "row",
			elevation: 3,
		},
		text: {
			marginLeft: "5%",
			textAlign: "center",
			textAlignVertical: "center",
			fontSize: 20,
		},
		subScribe: {
			flexDirection: "row",
		},
		subScribeText: {
			marginLeft: "5%",
			textAlign: "center",
			textAlignVertical: "center",
			fontSize: 20,
			marginRight: 0,
			paddingRight: 0,
		},
		subScribeBox: {
			marginLeft: 0,
			paddingLeft: 0,
		},
	});
} else {
	styles = StyleSheet.create({
		header: {
			width: "100%",
			height: "8.5%",
			backgroundColor: "white",
			alignItems: "center",
			justifyContent: "space-between",
			flexDirection: "row",
			shadowColor: "#000000",
			shadowOpacity: 0.3,
			shadowOffset: { width: 2, height: 2 },
		},
		text: {
			marginLeft: "5%",
			textAlign: "center",
			textAlignVertical: "center",
			fontSize: 20,
		},
	});
}

export default ScreenHeader;
