import React, { useState, useEffect } from "react";
import { View, StyleSheet } from "react-native";
import CardComponent from "../components/Card";
import ButtonModal from "../components/ButtonModal";
import SearchModal from "../components/SearchModal";
import ScreenHeader from "../components/ScreenHeader";
import setting from "../../setting.json";

const Main = (props) => {
	const [visible1, setVisible1] = useState(false);
	const [visible2, setVisible2] = useState(false);
	const [current, setCurrent] = useState("All");
	const [text, setText] = useState("");
	const [tempText, setTempText] = useState("");
	const [fromFirst, setFromFirst] = useState(1);
	const [categoryLabel, setCategoryLabel] = useState("모두");

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
				screenName="메인화면"
				FsetVisible1={setVisible1}
				FsetVisible2={setVisible2}
				categoryLabelValue={categoryLabel}
				navigation={props.navigation}
			/>
			<CardComponent
				pressName="Main"
				pressURL={setting["URL"] + "read_busan/"}
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

export default Main;
