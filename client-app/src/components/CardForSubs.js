import React, { useState, useEffect, useRef } from "react";
import {
	Text,
	View,
	StyleSheet,
	FlatList,
	TouchableOpacity,
} from "react-native";
import { Card } from "react-native-elements/dist/card/Card";
import {
	getUrl,
	loadDataForSubs,
	loadExtraDataForSubs,
	toTop,
	setFalse,
	setTrue,
} from "../functions/functions";
import ArticleModal from "./ArticleModal";

const CardComponentForSubs = (props) => {
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [prevText, setPrevText] = useState("");
	const [prevCategory, setPrevCategory] = useState("All");
	const [firstParam, setFirstParam] = useState(5);
	const [secondParam, setSecondParam] = useState(9);
	const [fromFirst, setFromFirst] = useState(1);
	const [url, setUrl] = useState([]);
	const [reset, setReset] = useState(1);

	const flatListRef = useRef();

	if (fromFirst !== props.fromFirst) {
		setFromFirst(props.fromFirst);
	}

	if (prevText !== props.search) {
		setPrevText(props.search);
	}

	if (prevCategory !== props.category) {
		setPrevCategory(props.category);
	}

	if (reset !== props.reset) {
		setReset(props.reset);
	}

	useEffect(() => {
		getUrl().then((urls) => {
			for (let i = 0; i < urls.length; i++) {
				loadDataForSubs(
					urls[i],
					props.search,
					props.category,
					setLoading,
					setData,
					data
				);
			}
			setUrl(urls);
		});
		setFirstParam(5);
		setSecondParam(9);
	}, []);

	useEffect(() => {
		setLoading(true);
		getUrl().then((urls) => {
			for (let i = 0; i < urls.length; i++) {
				loadDataForSubs(
					urls[i],
					props.search,
					props.category,
					setLoading,
					setData,
					data
				);
			}
			setUrl(urls);
		});
		setFirstParam(5);
		setSecondParam(9);
		toTop(flatListRef);
	}, [prevText, prevCategory, reset]);

	useEffect(() => {
		toTop(flatListRef);
	}, [fromFirst]);

	const Item = ({ item }) => {
		return (
			<View>
				<ArticleModal
					item={item}
					FsetFalse={setFalse}
					data={data}
					FsetData={setData}
				/>
				<TouchableOpacity
					onPress={() => setTrue(item.id, data, setData)}
				>
					<Card>
						<Text>{item.press}</Text>
						<Text style={{ fontSize: 20 }}>{item.title}</Text>
						<Text></Text>
						<Text numberOfLines={3}>{item.mainText}</Text>
					</Card>
				</TouchableOpacity>
			</View>
		);
	};

	return (
		<View style={styles.container}>
			<FlatList
				style={{ width: "100%" }}
				data={data}
				renderItem={(item) => {
					return Item(item, data, setData);
				}}
				onRefresh={() => {
					for (let i = 0; i < url.length; i++) {
						loadDataForSubs(
							url[i],
							props.search,
							props.category,
							setLoading,
							setData,
							data
						);
					}
				}}
				refreshing={loading}
				keyExtractor={(item) => item.id}
				onEndReached={() => {
					setLoading(true);
					for (let i = 0; i < url.length; i++) {
						loadExtraDataForSubs(
							url[i],
							data,
							firstParam,
							secondParam,
							setLoading,
							prevText,
							prevCategory,
							setData
						);
					}
					setFirstParam(secondParam + 1);
					setSecondParam(secondParam + 5);
				}}
				onEndReachedThreshold={0.9}
				ref={flatListRef}
			/>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		alignContent: "center",
		alignItems: "center",
		width: "100%",
	},
	titleStyle2: {
		fontSize: 20,
	},
});

export default CardComponentForSubs;
