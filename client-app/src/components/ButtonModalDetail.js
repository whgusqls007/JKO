import React, { useState, useEffect } from "react";
import { View, StyleSheet, Text, CheckBox } from "react-native";
import { AntDesign } from "@expo/vector-icons";
import RadioButton from "expo-radio-button";
import { getItemFromAsync, setItemToAsync } from "../functions/functions";
import Toast from "react-native-root-toast";

const ButtonModalDetail = (props) => {
	const [isSelected, setSelection] = useState(false);

	useEffect(() => {
		getItemFromAsync(props.name).then((data) => {
			if (data !== null) {
				if (data.saved === props.name) {
					setSelection(true);
				} else if (data.saved === true) {
					setSelection(false);
					setItemToAsync(props.name, { saved: false });
				} else {
					setSelection(false);
				}
			} else {
				setSelection(false);
				setItemToAsync(props.name, { saved: false });
			}
		});
	}, []);

	useEffect(() => {
		getItemFromAsync(props.name).then((data) => {
			if (data !== null) {
				if (data.saved === props.name && isSelected === false) {
					setItemToAsync(props.name, { saved: false }).then(() => {
						Toast.show(
							props.pressName + " 구독을 취소하였습니다.",
							{
								duration: Toast.durations.SHORT,
							}
						);
					});
				} else if (data.saved === false && isSelected === true) {
					setItemToAsync(props.name, { saved: props.name }).then(
						() => {
							Toast.show(props.pressName + " 구독 하였습니다.", {
								duration: Toast.durations.SHORT,
							});
						}
					);
				} else if (data.saved === false && isSelected === false) {
					setItemToAsync(props.name, { saved: false }).then(() => {});
				} else if (data.saved === props.name && isSelected === true) {
					setItemToAsync(props.name, { saved: props.name }).then(
						() => {}
					);
				}
			} else {
				setItemToAsync(props.name, { saved: false });
			}
		});
	}, [isSelected]);

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
				<View style={styles.subScribe}>
					<CheckBox
						value={isSelected}
						onValueChange={setSelection}
						style={styles.subScribeBox}
					/>
					<Text style={styles.subScribeText}>구독</Text>
				</View>
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

export default ButtonModalDetail;
