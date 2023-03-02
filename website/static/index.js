// sending a post request to delete a student from the database
function deleteStudent(studentId) {
    fetch("/delete-student", {
        // when clicked it send the information to the delete-student function
        method: "POST",
        body: JSON.stringify({ studentId: studentId }),
    }).then((_res) => {
        // reload the webpage
        window.location.href = "/";
    });
}

// sending a post request to delete an instructor from the database
function deleteInstructor(instructorId) {
    fetch("/delete-instructor", {
        // when clicked it send the information to the delete-instructor function
        method: "POST",
        body: JSON.stringify({ instructorId: instructorId }),
    }).then((_res) => {
        // reload the webpage
        window.location.href = "/instructor";
    });
}

// sending a post request to delete an course from the database
function deleteCourse(courseId) {
    fetch("/delete-course", {
        // when clicked it send the information to the delete-course function
        method: "POST",
        body: JSON.stringify({ courseId: courseId }),
    }).then((_res) => {
        // reload the webpage
        window.location.href = "/course";
    });
}

// sending a post request to delete an enrollment from the database
function deleteEnrollment(enrollmentId) {
    console.log(enrollmentId)
    fetch("/delete-enrollment", {
        // when clicked it send the information to the delete-enrollment function
        method: "POST",
        body: JSON.stringify({ enrollmentId: enrollmentId }),
    }).then((_res) => {
        // reload the webpage
        window.location.href = "/enrollment";
    });
}

