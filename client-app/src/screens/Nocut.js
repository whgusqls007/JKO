import React, { useState, useEffect } from "react";
import { View, StyleSheet, BackHandler } from "react-native";
import CardComponent from "../components/Card";
import ButtonModal from "../components/ButtonModal";
import SearchModal from "../components/SearchModal";
import ScreenHeader from "../components/ScreenHeader";
import setting from "../../setting.json";
import { CategoryLabel } from "../functions/functions";

const Nocut = (props) => {
	const [visible1, setVisible1] = useState(false);
	const [visible2, setVisible2] = useState(false);
	const [current, setCurrent] = useState("All");
	const [text, setText] = useState("");
	const [tempText, setTempText] = useState("");
	const [fromFirst, setFromFirst] = useState(1);
	const [categoryLabel, setCategoryLabel] = useState("모두");
	const [reset, setReset] = useState(0);

	useEffect(() => {
		const backAction = () => {
			setCurrent("All");
			setText("");
			setTempText("");
			if (fromFirst === 1) {
				setFromFirst(0);
			} else {
				setFromFirst(1);
			}
			props.navigation.navigate("Main");
			return true;
		};

		const backHandler = BackHandler.addEventListener(
			"hardwareBackPress",
			backAction
		);

		return () => backHandler.remove();
	}, []);

	useEffect(() => {
		CategoryLabel(current, setCategoryLabel);
	}, [current]);

	return (
		<View style={styles.container}>
			<ButtonModal
				FsetVisible={setVisible1}
				FsetCurrent={setCurrent}
				currentValue={current}
				visibleValue={visible1}
				name="read_nocut/"
				pressName="노컷뉴스"
			/>
			<SearchModal
				visibleValue={visible2}
				FsetVisible={setVisible2}
				FsetTempText={setTempText}
				tempTextValue={tempText}
				FsetText={setText}
				FsetVisible={setVisible2}
				FsetReset={setReset}
				reset={reset}
			/>
			<ScreenHeader
				screenName="노컷뉴스"
				FsetVisible1={setVisible1}
				FsetVisible2={setVisible2}
				categoryLabelValue={categoryLabel}
				navigation={props.navigation}
				FsetReset={setReset}
				reset={reset}
			/>
			<CardComponent
				pressName="read_nocut/"
				pressURL={setting["URL"] + "read_nocut/"}
				search={text}
				category={current}
				fromFirst={fromFirst}
				reset={reset}
			/>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: "center",
		alignItems: "center",
	},
});

export default Nocut;
