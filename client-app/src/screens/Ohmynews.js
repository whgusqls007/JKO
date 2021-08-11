import React, { useState, useEffect } from "react";
import { View, StyleSheet, BackHandler } from "react-native";
import CardComponent from "../components/Card";
import ButtonModal from "../components/ButtonModal";
import SearchModal from "../components/SearchModal";
import ScreenHeader from "../components/ScreenHeader";
import setting from "../../setting.json";

const Ohmynews = (props) => {
	const [visible1, setVisible1] = useState(false);
	const [visible2, setVisible2] = useState(false);
	const [current, setCurrent] = useState("All");
	const [text, setText] = useState("");
	const [tempText, setTempText] = useState("");
	const [fromFirst, setFromFirst] = useState(1);
	const [categoryLabel, setCategoryLabel] = useState("모두");

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
			props.navigation.goBack();
			return true;
		};

		const backHandler = BackHandler.addEventListener(
			"hardwareBackPress",
			backAction
		);

		return () => backHandler.remove();
	}, []);

	useEffect(() => {
		if (current === "All") {
			setCategoryLabel("모두");
		} else if (current === "sports") {
			setCategoryLabel("스포츠");
		} else if (current === "politic") {
			setCategoryLabel("정치");
		} else if (current === "society") {
			setCategoryLabel("사회");
		} else {
			setCategoryLabel("경제");
		}
	}, [current]);

	return (
		<View style={styles.container}>
			<ButtonModal
				FsetVisible={setVisible1}
				FsetCurrent={setCurrent}
				currentValue={current}
				visibleValue={visible1}
			/>
			<SearchModal
				visibleValue={visible2}
				FsetVisible={setVisible2}
				FsetTempText={setTempText}
				tempTextValue={tempText}
				FsetText={setText}
				FsetVisible={setVisible2}
			/>
			<ScreenHeader
				screenName="오마이뉴스"
				FsetVisible1={setVisible1}
				FsetVisible2={setVisible2}
				categoryLabelValue={categoryLabel}
				navigation={props.navigation}
			/>
			<CardComponent
				pressName="ohmynews"
				pressURL={setting["URL"] + "read_ohmynews/"}
				search={text}
				category={current}
				fromFirst={fromFirst}
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

export default Ohmynews;
