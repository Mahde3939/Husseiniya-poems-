import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Alert } from 'react-native';

const App = () => {
  // قائمة التصنيفات
  const categories = [
    { id: '1', title: 'محرم' },
    { id: '2', title: 'أربعين' },
    { id: '3', title: 'رثاء' },
    { id: '4', title: 'مديح' },
  ];

  // دالة لعرض القصائد عند النقر على التصنيف
  const handleCategoryPress = (categoryTitle) => {
    // عرض رسالة بمحتوى التصنيف (يمكنك هنا وضع القصائد الخاصة بكل تصنيف)
    Alert.alert(`قصائد تصنيف: ${categoryTitle}`, 'هنا ستعرض القصائد الخاصة بهذا التصنيف.');
  };

  // دالة لعرض التصنيف
  const renderCategory = ({ item }) => (
    <TouchableOpacity 
      style={styles.categoryButton} 
      onPress={() => handleCategoryPress(item.title)}
    >
      <Text style={styles.categoryText}>{item.title}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>قصائد حسينية</Text>
      <FlatList
        data={categories}
        renderItem={renderCategory}
        keyExtractor={item => item.id}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a1a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    fontSize: 24,
    color: '#fff',
    marginBottom: 20,
    fontWeight: 'bold',
  },
  categoryButton: {
    backgroundColor: '#333',
    padding: 15,
    margin: 10,
    borderRadius: 5,
    width: '80%',
  },
  categoryText: {
    fontSize: 18,
    color: '#fff',
    textAlign: 'center',
  },
});

export default App;
