import React from "react";
import { View, StyleSheet, Text, CheckBox } from "react-native";
import { AntDesign } from "@expo/vector-icons";
import RadioButton from "expo-radio-button";

const ButtonModalDetailForSubs = (props) => {
	return (
		<View style={{ backgroundColor: "white" }}>
			<View style={{ flexWrap: "nowrap" }}>
				<Text style={styles.textstyle}>카테고리</Text>
				<View style={styles.radioButtonView}>
					<RadioButton
						value="politics"
						selected={props.currentValue}
						onSelected={(value) => {
							props.FsetCurrent(value);
							props.FsetVisible(false);
						}}
						radioBackground="blue"
					>
						<Text>정치</Text>
					</RadioButton>
					<RadioButton
						value="economy"
						selected={props.currentValue}
						onSelected={(value) => {
							props.FsetCurrent(value);
							props.FsetVisible(false);
						}}
						radioBackground="blue"
					>
						<Text>경제</Text>
					</RadioButton>
					<RadioButton
						value="society"
						selected={props.currentValue}
						onSelected={(value) => {
							props.FsetCurrent(value);
							props.FsetVisible(false);
						}}
						radioBackground="blue"
					>
						<Text>사회</Text>
					</RadioButton>
					<RadioButton
						value="sport"
						selected={props.currentValue}
						onSelected={(value) => {
							props.FsetCurrent(value);
							props.FsetVisible(false);
						}}
						radioBackground="blue"
					>
						<Text>스포츠</Text>
					</RadioButton>
					<RadioButton
						value="All"
						selected={props.currentValue}
						onSelected={(value) => {
							props.FsetCurrent(value);
							props.FsetVisible(false);
						}}
						radioBackground="blue"
					>
						<Text>모두</Text>
					</RadioButton>
				</View>
			</View>
			<View style={styles.closecircleView}>
				<AntDesign.Button
					name="closecircle"
					size={24}
					color="black"
					style={{ backgroundColor: "white" }}
					onPress={() => props.FsetVisible(false)}
				>
					<Text>닫기</Text>
				</AntDesign.Button>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	closecircleView: {
		marginLeft: "auto",
		flexDirection: "row",
		marginTop: "2%",
		marginRight: "2%",
		textAlignVertical: "center",
		alignContent: "center",
		justifyContent: "center",
	},
	radioButtonView: {
		flexDirection: "row",
		justifyContent: "space-between",
		paddingLeft: 30,
		paddingRight: 30,
		paddingTop: 20,
	},
	textstyle: {
		paddingLeft: 30,
		paddingTop: 30,
		fontSize: 20,
	},
	subScribe: {
		flexDirection: "row",
	},
	subScribeText: {
		marginLeft: "5%",
		textAlign: "center",
		textAlignVertical: "center",
		marginRight: 0,
		marginTop: "auto",
		marginBottom: "auto",
		paddingRight: 0,
	},
	subScribeBox: {
		margin: 0,
		marginTop: "auto",
		marginBottom: "auto",
		padding: 0,
	},
});

export default ButtonModalDetailForSubs;
