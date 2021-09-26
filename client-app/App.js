import 'react-native-gesture-handler';
import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { NavigationContainer } from '@react-navigation/native';
import DrawerNavigator from './src/navigators/DrawerScreen';
import { SafeAreaView } from 'react-native';
import Constants from 'expo-constants';
import { RootSiblingParent } from 'react-native-root-siblings';

const App = () => {
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
